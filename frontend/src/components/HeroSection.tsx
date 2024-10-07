'use client';

import { FC } from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';

const HeroSection: FC = () => {
  return (
    <section className="relative bg-gray-900 text-white">
      <div className="container mx-auto px-6 py-32 text-center">
        <motion.h1
          className="text-5xl font-bold leading-tight"
          initial={{ opacity: 0, y: -50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          Unlock Your Potential with Our Product
        </motion.h1>
        <motion.p
          className="mt-6 text-xl"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 0.8 }}
        >
          Join thousands of users in taking the next step in being an
          entrepreneur.
        </motion.p>
        <motion.div
          className="mt-10"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 1, duration: 0.8 }}
        >
          <Link
            href="/items"
            className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-semibold py-4 px-8 rounded"
          >
            View Dashboard
          </Link>
        </motion.div>
      </div>
    </section>
  );
};

export default HeroSection;
