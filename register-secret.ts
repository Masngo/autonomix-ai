import { registerEntitySecretCiphertext } from '@circle-fin/developer-controlled-wallets';
import 'dotenv/config';

const apiKey = process.env.CIRCLE_API_KEY;
const entitySecret = process.env.CIRCLE_ENTITY_SECRET;

if (!apiKey || !entitySecret) {
  console.error("❌ Error: CIRCLE_API_KEY and CIRCLE_ENTITY_SECRET must be set in .env");
  process.exit(1);
}

async function register() {
  try {
    console.log("Registering Entity Secret with Circle...");
    const response = await registerEntitySecretCiphertext({
      apiKey,
      entitySecret,
    });
    console.log("✅ Entity Secret registered successfully!");
    console.log("Save your recovery file contents:\n", response.data?.recoveryFile);
  } catch (error) {
    console.error("❌ Registration failed:", error);
  }
}

register();
