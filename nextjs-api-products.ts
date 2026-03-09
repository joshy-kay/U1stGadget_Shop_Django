import { NextRequest, NextResponse } from 'next/server';
import connectDB from '@/lib/mongodb';
import Product from '@/models/Product';

// Sample products data (will be replaced with database)
const sampleProducts = [
  {
    _id: '1',
    name: 'Galaxy S Ultra',
    description: 'Flagship smartphone with brilliant display',
    price: 1299.99,
    category: 'Phones',
    image: 'https://via.placeholder.com/300x300?text=Galaxy+S+Ultra',
    stock: 10,
    featured: true,
  },
  {
    _id: '2',
    name: 'ProBook 14 Laptop',
    description: 'Lightweight laptop for professionals',
    price: 899.99,
    category: 'Laptops',
    image: 'https://via.placeholder.com/300x300?text=ProBook+14',
    stock: 5,
    featured: true,
  },
  {
    _id: '3',
    name: 'NoiseCancel Pro',
    description: 'Premium noise-cancelling headphones',
    price: 199.99,
    category: 'Audio',
    image: 'https://via.placeholder.com/300x300?text=NoiseCancel+Pro',
    stock: 15,
    featured: false,
  },
];

export async function GET() {
  try {
    // For now, return sample data
    // Later: await connectDB(); const products = await Product.find({});
    return NextResponse.json({
      success: true,
      products: sampleProducts,
      message: 'Sample products loaded successfully'
    });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch products', success: false },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    // Later: await connectDB(); const product = await Product.create(body);
    return NextResponse.json({
      success: true,
      message: 'Product created (sample)',
      product: body
    });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create product', success: false },
      { status: 500 }
    );
  }
}