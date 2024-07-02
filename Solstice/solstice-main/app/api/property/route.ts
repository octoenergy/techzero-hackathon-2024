"use server";
import PropertyModel from "../../models/property.model";
import { connectToMongoDB } from "../../libs/mongodb.lib";
import { NextRequest, NextResponse } from "next/server";

/**
 *
 */
export const GET = async (req: NextRequest) => {
  await connectToMongoDB();
  try {
    const properties = await PropertyModel.find();
    return NextResponse.json(properties, { status: 200 });
  } catch (err) {
    console.error(err);
    return NextResponse.json(
      { message: (err as any).message },
      { status: 400 }
    );
  }
};
