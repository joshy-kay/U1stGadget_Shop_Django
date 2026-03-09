import Link from 'next/link'

export default function Home() {
  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <div className="hero min-h-[60vh] bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">Welcome to U1st Gadget & Things</h1>
            <p className="py-6">
              Discover the latest electronics, phones, computers, and tech gadgets at unbeatable prices!
            </p>
            <Link href="/products" className="btn btn-primary btn-lg">
              Shop Now 🛒
            </Link>
          </div>
        </div>
      </div>

      {/* Features */}
      <div className="container mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="card bg-base-100 shadow-xl">
            <div className="card-body items-center text-center">
              <div className="text-6xl">📱</div>
              <h2 className="card-title">Latest Phones</h2>
              <p>Premium smartphones and accessories</p>
            </div>
          </div>

          <div className="card bg-base-100 shadow-xl">
            <div className="card-body items-center text-center">
              <div className="text-6xl">💻</div>
              <h2 className="card-title">Gaming Laptops</h2>
              <p>High-performance computers for work and play</p>
            </div>
          </div>

          <div className="card bg-base-100 shadow-xl">
            <div className="card-body items-center text-center">
              <div className="text-6xl">🎧</div>
              <h2 className="card-title">Audio Gear</h2>
              <p>Premium headphones and speakers</p>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="bg-primary text-primary-content py-16">
        <div className="container mx-auto text-center px-4">
          <h2 className="text-4xl font-bold mb-4">Ready to Shop?</h2>
          <p className="text-xl mb-8">Join thousands of satisfied customers</p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/products" className="btn btn-secondary btn-lg">
              Browse Products
            </Link>
            <Link href="/admin" className="btn btn-outline btn-lg">
              Admin Dashboard
            </Link>
          </div>
        </div>
      </div>
    </main>
  )
}