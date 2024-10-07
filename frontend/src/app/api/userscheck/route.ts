import { NextRequest, NextResponse } from 'next/server';

export const maxDuration = 300;
export async function POST(request: NextRequest) {
  const requestData = await request.json();

  const res = await fetch(`${process.env.NEXT_API_BASE_URL}users/check`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.ACCESS_TOKEN}`,
    },
    body: JSON.stringify({
      email: requestData.email,
    }),
  });
  const data = await res.json();

  return NextResponse.json(data);
}
