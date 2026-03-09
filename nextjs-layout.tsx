import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'U1st Gadget & Things',
  description: 'Your one-stop shop for electronics and gadgets',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav className="navbar bg-base-100 shadow-lg">
          <div className="navbar-start">
            <a className="btn btn-ghost normal-case text-xl">🎯 U1st Gadget Shop</a>
          </div>
          <div className="navbar-center">
            <ul className="menu menu-horizontal px-1">
              <li><a href="/">Home</a></li>
              <li><a href="/products">Products</a></li>
              <li><a href="/admin">Admin</a></li>
            </ul>
          </div>
          <div className="navbar-end">
            <a className="btn btn-primary">Login</a>
          </div>
        </nav>
        {children}
      </body>
    </html>
  )
}