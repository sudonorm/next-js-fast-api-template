'use client';

import { FC } from 'react';
import Link from 'next/link';

const CallToActionSection: FC = () => {
  return (
    <section className="bg-blue-600 text-white py-20">
      <div className="container mx-auto px-6 text-center">
        <h2 className="text-4xl font-bold">Ready to Get Started?</h2>
        <p className="mt-4 text-xl">Sign up today and unlock full access.</p>
        <Link
          href="/auth/register"
          className="mt-6 inline-block bg-white text-blue-600 font-semibold py-4 px-8 rounded"
        >
          Register Now
        </Link>
      </div>
    </section>
  );
};

export default CallToActionSection;
