import { FC } from 'react';

interface TestimonialProps {
  quote: string;
  author: string;
}

const TestimonialCard: FC<TestimonialProps> = ({ quote, author }) => {
  return (
    <div className="bg-white p-8 rounded shadow">
      <p className="text-gray-600 italic">"{quote}"</p>
      <h4 className="mt-4 font-semibold">- {author}</h4>
    </div>
  );
};

export default TestimonialCard;
