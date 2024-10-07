'use client';

import { createContext, ReactNode, useContext } from 'react';
import axios from 'axios';
import { AxiosRequestConfig, AxiosRequestHeaders } from 'axios';
import { redirect } from 'next/navigation';
import { useSession, signIn } from 'next-auth/react';
import { useRouter } from 'next/navigation';

type ApiProviderProps = {
  children: ReactNode;
};

type ApiContextType = {
  getUsersMe: (status: any) => Promise<any>;
  signUp: (
    email: string,
    first_name: string,
    last_name: string,
    password: string
  ) => Promise<any>;
  getItems: () => Promise<any>;
};

export const ApiContext = createContext<ApiContextType | undefined>(undefined);

export function ApiProvider({ children }: ApiProviderProps) {
  async function handleRequestError(error: any) {
    if (error.response && error.response.status === 401) {
      console.log('Unauthorized access - 401');
    }
  }

  async function getUsersMe(status: any): Promise<any> {
    const router = useRouter();

    try {
      if (status === 'authenticated' || status === 'loading') {
        const response = await axios.get('/api/users', {});
        const usersData = response.data;
        return usersData;
      } else {
        router.push('auth/login');
      }
    } catch (error: any) {
      handleRequestError(error);
      return [];
    }
  }

  async function getItems(): Promise<any> {
    console.log('in get items');
    try {
      const response = await axios.get('/api/items', {});
      console.log('response:', response);
      const itemsData = response.data;

      console.log(itemsData);
      return itemsData;
    } catch (error: any) {
      handleRequestError(error);
      return [];
    }
  }

  async function signUp(
    email: string,
    first_name: string,
    last_name: string,
    password: string
  ): Promise<any> {
    try {
      const response = await axios.post('/api/register', {
        email,
        first_name,
        last_name,
        password,
      });
      const usersData = response.data;
      return usersData;
    } catch (error: any) {
      handleRequestError(error);
      return [];
    }
  }

  const apiContextValue: ApiContextType = {
    getUsersMe,
    signUp,
    getItems,
  };

  return (
    <ApiContext.Provider value={apiContextValue}>
      {children}
    </ApiContext.Provider>
  );
}

export function useApi() {
  const context = useContext(ApiContext);
  if (!context) {
    throw new Error('useApi must be used within an ApiProvider');
  }
  return context;
}
