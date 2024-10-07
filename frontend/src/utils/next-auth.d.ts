import NextAuth from 'next-auth';

declare module 'next-auth' {
  interface Session {
    user: {
      id: string;
      name?: string | null;
      email?: string | null;
      accessToken?: string;
      [key: string]: any;
    };
    error?: string;
  }

  interface User {
    id: string;
    name?: string | null;
    email?: string | null;
    accessToken?: string;
    refreshToken?: string;
    [key: string]: any;
  }
}

declare module 'next-auth/jwt' {
  interface JWT {
    id?: string;
    accessToken?: string;
    refreshToken?: string;
    accessTokenExpires?: number;
    error?: string;
    [key: string]: any;
  }
}
