'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useApi } from '@/contexts/api/api.context';

export default function RegisterPage() {
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');

  const router = useRouter();
  const api = useApi();

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      api.signUp(email, firstName, lastName, password).then((response) => {});
      router.push('/');
    } catch (error: any) {
      console.error(
        'Registration failed:',
        error.response?.data?.detail || error.message
      );
    }
  };

  return (
    <div>
      <h1 className="text-2xl font-bold">Register</h1>
      <form onSubmit={handleRegister} className="mt-4 space-y-4">
        <input
          type="text"
          placeholder="First Name"
          className="w-full border p-2 rounded"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Last Name"
          className="w-full border p-2 rounded"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          className="w-full border p-2 rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full border p-2 rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded"
        >
          Register
        </button>
      </form>
    </div>
  );
}
