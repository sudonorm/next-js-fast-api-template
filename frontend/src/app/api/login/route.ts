import { NextRequest, NextResponse } from 'next/server';

export const maxDuration = 300;
export async function POST(request: NextRequest) {
  const requestData = await request.json();

  const res = await fetch(`${process.env.API_BASE_URL}users/token`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email: requestData.email,
      password: requestData.password,
    }),
  });

  const data = await res.json();

  const response = NextResponse.json(data);

  return response;
}
