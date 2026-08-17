import { initiateDeveloperControlledWalletsClient } from '@circle-fin/developer-controlled-wallets';
import 'dotenv/config';

const apiKey = process.env.CIRCLE_API_KEY;
const entitySecret = process.env.CIRCLE_ENTITY_SECRET;

if (!apiKey || !entitySecret) {
  console.error("Error: CIRCLE_API_KEY and CIRCLE_ENTITY_SECRET must be set in .env");
  process.exit(1);
}

const client = initiateDeveloperControlledWalletsClient({
  apiKey,
  entitySecret,
});

async function createWallet() {
  try {
    console.log("Creating Wallet Set...");
    const walletSetResponse = await client.createWalletSet({
      name: 'Autonomix Wallet Set',
    });

    const walletSetId = walletSetResponse.data?.walletSet?.id;
    console.log("✅ Created Wallet Set ID:", walletSetId);

    if (walletSetId) {
      console.log("Creating Developer-Controlled Wallet...");
      const walletResponse = await client.createWallets({
        blockchains: ['BASE-SEPOLIA'],
        count: 1,
        walletSetId,
      });

      console.log("\n✅ Wallet Created Successfully!");
      console.log(JSON.stringify(walletResponse.data, null, 2));
    }
  } catch (error) {
    console.error("❌ Error creating wallet:", error);
  }
}

createWallet();
