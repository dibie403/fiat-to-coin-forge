/**
 * Mock Paystack service. Replace with the real Paystack SDK later.
 */
const delay = (ms = 700) => new Promise((r) => setTimeout(r, ms));

export interface PaystackInitResponse {
  reference: string;
  authorization_url: string; // would normally redirect; we simulate
  access_code: string;
}

export async function initializePayment(input: {
  email: string;
  amount: number; // NGN, in whole units
  metadata?: Record<string, unknown>;
}): Promise<PaystackInitResponse> {
  await delay();
  const reference = "pst_mock_" + Math.random().toString(36).slice(2, 12);
  return {
    reference,
    authorization_url: "#mock-paystack-checkout",
    access_code: "ac_" + reference,
  };
}

export async function verifyPayment(reference: string): Promise<{
  status: "success" | "failed";
  reference: string;
}> {
  await delay(900);
  // 95% success in mock
  return { status: Math.random() > 0.05 ? "success" : "failed", reference };
}
