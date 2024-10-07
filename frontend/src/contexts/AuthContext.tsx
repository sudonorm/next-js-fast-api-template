'use client';

import React, { createContext, useState, useEffect, FC } from 'react';
import { useRouter } from 'next/navigation';
import { useApi } from '@/contexts/api/api.context';
import { redirect } from 'next/navigation';
import { useSession, signIn } from 'next-auth/react';

interface User {
  id: number | undefined;
  email: string | undefined;
}

interface AuthContextProps {
  user: Object | undefined;
}

export const AuthContext = createContext<AuthContextProps>({
  user: undefined,
});

export const AuthProvider: FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const router = useRouter();
  const api = useApi();

  const { data: session, status } = useSession();
  const token: string | undefined = session?.user?.accessToken;
  const user: Object | undefined = session?.user;

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/');
    }
  });

  return (
    <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>
  );
};
