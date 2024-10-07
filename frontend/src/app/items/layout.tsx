export default function ItemsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section className="container mx-auto p-4">
      <h1 className="text-3xl font-bold">Dashboard</h1>
      {children}
    </section>
  );
}
