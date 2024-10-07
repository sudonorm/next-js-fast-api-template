'use client';
import Link from 'next/link';
import { FC } from 'react';
import HeroSection from '../components/HeroSection';
import FeaturesSection from '../components/FeaturesSection';
import TestimonialsSection from '../components/TestimonialsSection';
import CallToActionSection from '../components/CallToActionSection';
import { useSession } from 'next-auth/react';

const LandingPage: FC = () => {
  const { data: session, status } = useSession();
  return (
    <>
      <HeroSection />
      <FeaturesSection />
      <TestimonialsSection />
      {session?.user ? <> </> : <CallToActionSection />}
    </>
  );
};

export default LandingPage;
