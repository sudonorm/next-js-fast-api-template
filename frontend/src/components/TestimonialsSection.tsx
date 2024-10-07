'use client';

import { FC } from 'react';
import TestimonialCard from './TestimonialCard';

const TestimonialsSection: FC = () => {
  const testimonials = [
    {
      quote: 'This product changed my life. I highly recommend it',
      author: 'Jane Doe',
    },
    {
      quote: 'A fantastic product with practical use-cases.',
      author: 'John Smith',
    },
    {
      quote:
        'Highly recommend this product anyone looking to advance themselves.',
      author: 'Alice Johnson',
    },
  ];

  return (
    <section className="bg-gray-100 py-20">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl font-bold text-center mb-12">
          What Our Clients Say
        </h2>
        <div className="flex flex-wrap -mx-6">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="w-full md:w-1/3 px-6 mb-12 md:mb-0">
              <TestimonialCard
                quote={testimonial.quote}
                author={testimonial.author}
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;
