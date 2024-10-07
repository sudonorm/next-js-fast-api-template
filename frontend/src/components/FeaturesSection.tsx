'use client';

import { FC } from 'react';
import Feature from './Feature';
import { FaChalkboardTeacher, FaBookOpen, FaCertificate } from 'react-icons/fa';

const FeaturesSection: FC = () => {
  return (
    <section className="container mx-auto px-6 py-20">
      <div className="flex flex-wrap -mx-6">
        <Feature
          title="Expert Sellers"
          description="Learn from industry experts who are passionate about their craft."
          icon={<FaChalkboardTeacher className="text-blue-600 text-4xl" />}
        />
        <Feature
          title="Comprehensive Content"
          description="Access a wide range of items covering various products."
          icon={<FaBookOpen className="text-blue-600 text-4xl" />}
        />
        <Feature
          title="Certified Products"
          description="Products come with appropriate certificates."
          icon={<FaCertificate className="text-blue-600 text-4xl" />}
        />
      </div>
    </section>
  );
};

export default FeaturesSection;
