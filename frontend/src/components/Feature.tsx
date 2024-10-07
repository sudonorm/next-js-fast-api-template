import { FC, ReactElement } from 'react';

interface FeatureProps {
  title: string;
  description: string;
  icon: ReactElement;
}

const Feature: FC<FeatureProps> = ({ title, description, icon }) => {
  return (
    <div className="w-full md:w-1/3 px-6 mb-12 md:mb-0">
      <div className="text-center">
        <div className="inline-flex items-center justify-center w-20 h-20 mb-6 rounded-full bg-blue-100">
          {icon}
        </div>
        <h3 className="text-2xl font-semibold mb-4">{title}</h3>
        <p className="text-gray-600">{description}</p>
      </div>
    </div>
  );
};

export default Feature;
