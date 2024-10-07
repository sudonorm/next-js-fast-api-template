import type { User } from '@/types/user';
import axios from 'axios';
import { AxiosRequestConfig, AxiosRequestHeaders } from 'axios';

const API_BASE_URL = process.env.API_BASE_URL;

export async function verifyUserCredentials(
  email: string,
  password: string
): Promise<User | null> {
  async function handleRequestError(error: any) {
    if (error.response && error.response.status === 404) {
      console.log('User not found');
    }
  }

  const response = await axios.post(`${API_BASE_URL}users/check`, { email }, {
    headers: {
      Authorization: `Bearer ${process.env.ACCESS_TOKEN}`,
    },
    withCredentials: true,
  } as AxiosRequestConfig);

  const userData = response.data;

  if (userData) {
    try {
      const responseLogin = await axios.post(
        `${API_BASE_URL}users/token`,
        { email, password },
        {
          withCredentials: true,
        } as AxiosRequestConfig
      );
      const responseData = responseLogin.data;

      const responseObj: User = Object();

      responseObj.id = userData.id;
      responseObj.name = userData.first_name + ' ' + userData.last_name;
      responseObj.accessToken = responseData.access_token;
      responseObj.email = email;
      responseObj.role = userData.is_superuser ? 'admin' : 'user';

      return responseObj;
    } catch (error: any) {
      handleRequestError(error);
      return null;
    }
  } else {
    return null;
  }
}
