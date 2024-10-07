'use client';

import { ApiProvider } from '@/contexts/api/api.context';
import { AuthProvider } from '@/contexts/AuthContext';
import { SessionProvider } from 'next-auth/react';

export function Providers({ children }: any) {
  return (
    <SessionProvider>
      <ApiProvider>
        <AuthProvider>{children}</AuthProvider>
      </ApiProvider>
    </SessionProvider>
  );
}
