export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <section className="container mx-auto p-4">{children}</section>;
}
