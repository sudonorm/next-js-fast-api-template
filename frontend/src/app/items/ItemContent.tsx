'use client';

import Link from 'next/link';
import { useState, useEffect } from 'react';
import { useApi } from '@/contexts/api/api.context';
import { useSession, signIn } from 'next-auth/react';
import { useRouter } from 'next/navigation';

interface Item {
  id: number;
  name: string;
  description: string;
  price: number;
  slugs: string;
}

export default function ItemContent() {
  const router = useRouter();
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(false);
  const api = useApi();
  const { data: session, status } = useSession();

  if (status === 'unauthenticated') {
    router.push('/auth/login');
  }

  useEffect(() => {
    // Fetch items data

    setLoading(true);
    api
      .getItems()
      .then((response) => {
        setItems(response);
        setLoading(false);
      }) //
      .catch((error) => {
        console.error('Error fetching items:', error);
        setLoading(false);
        setItems([]); // Fallback to empty array on error
      });
  }, []);

  return (
    <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
      {loading ? (
        <div>...Data Loading.....</div>
      ) : (
        items.map((item: Item) => (
          <div key={item.id} className="border p-4 rounded">
            <h2 className="text-xl font-semibold">{item.name}</h2>
            <p className="mt-2">{item.description}</p>
            <p className="mt-2 font-bold">Price: ${item.price}</p>

            <Link
              href={`${item.slugs}`}
              className="mt-4 inline-block bg-green-500 text-white px-4 py-2 rounded"
              style={{ pointerEvents: 'none' }}
            >
              View Item
            </Link>
          </div>
        ))
      )}
    </div>
  );
}
