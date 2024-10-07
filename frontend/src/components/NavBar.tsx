'use client';

import { FC, useContext } from 'react';
import Link from 'next/link';
import { AuthContext } from '../contexts/AuthContext';
import { useSession, signIn, signOut } from 'next-auth/react';

const NavBar: FC = () => {
  const { user } = useContext(AuthContext);
  const { data: session, status } = useSession();

  return (
    <nav className="bg-white shadow">
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-gray-800">
          Example Frontend
        </Link>
        <div className="flex items-center">
          {session?.user ? (
            <>
              <Link
                href="/items"
                className="text-gray-800 hover:text-blue-600 mx-4"
              >
                Dashboard
              </Link>
              <button
                onClick={() => signOut({ callbackUrl: '/', redirect: true })}
                className="text-gray-800 hover:text-red-600 mx-4"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link
                href="/auth/login"
                className="text-gray-800 hover:text-blue-600 mx-4"
              >
                Login
              </Link>
              <Link
                href="/auth/register"
                className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded"
              >
                Sign Up
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
