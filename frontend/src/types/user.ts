export interface User {
  id: string;
  name: string;
  email: string;
  role?: string;
  accessToken?: string;
}

export interface UserCheck {
  id: string;
  email: string;
}
