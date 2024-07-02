import mongoose, { Connection } from "mongoose";

let cachedConnection: Connection | null = null;

export async function connectToMongoDB() {
  if (cachedConnection) {
    return cachedConnection;
  }
  try {
    const cnx = await mongoose.connect(process.env.MONGO_DB_URI!);
    cachedConnection = cnx.connection;

    console.log("New mongodb connection established");

    return cachedConnection;
  } catch (error) {
    console.log(error);
    throw error;
  }
}
