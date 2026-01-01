/*************************************************
 * Karazon.com Billing & Checkout Module
 * SkillAssure University – SAHF Labs 1 to 13
 * Run in Browser Console
 *************************************************/

// -------------------- LAB 9: CUSTOM ERROR --------------------
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

// -------------------- LAB 10: CLOSURE FOR DISCOUNT --------------------
function getDiscountFunction(type) {
  const rates = {
    Silver: 0.05,
    Gold: 0.10,
    Platinum: 0.15
  };
  const rate = rates[type] || 0;

  return function (amount) {
    return amount * rate;
  };
}

// -------------------- LAB 12: INVENTORY PROMISE (FIXED) --------------------
function checkInventory(itemCode, quantity) {
  const inventory = {
    A101: 10,
    B202: 5,
    C303: 20
  };

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (inventory[itemCode] && inventory[itemCode] >= quantity) {
        resolve(true);
      } else {
        reject(new Error(`Insufficient stock for item ${itemCode}`));
      }
    }, 500);
  });
}

// -------------------- LAB 11: ASYNC PAYMENT --------------------
async function processPayment(mode) {
  console.log("Processing payment...");
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(`Payment successful via ${mode}`);
    }, 1500);
  });
}

// -------------------- LAB 13: CALLBACK --------------------
function completeBilling(callbackFn) {
  callbackFn();
}

// -------------------- MAIN BILLING FUNCTION --------------------
async function startBilling() {
  try {
    let cart = [];

    // -------- LAB 7: LOAD PREVIOUS CART --------
    let savedCart = localStorage.getItem("cartData");
    if (savedCart && confirm("Resume previous cart?")) {
      cart = JSON.parse(savedCart);
    } else {
      localStorage.clear();
    }

    // -------- LAB 1: ADD ITEMS TO CART --------
    let addMore = true;

    while (addMore) {
      let itemCode = prompt("Enter Item Code (A101/B202/C303):");
      let description = prompt("Enter Item Description:");
      let quantity = Number(prompt("Enter Quantity:"));
      let pricePerUnit = Number(prompt("Enter Price per Unit:"));

      if (quantity <= 0 || pricePerUnit <= 0) {
        throw new ValidationError("Quantity and price must be greater than 0");
      }

      await checkInventory(itemCode, quantity);

      let totalPrice = quantity * pricePerUnit;

      cart.push({
        itemCode,
        description,
        quantity,
        pricePerUnit,
        totalPrice
      });

      addMore = confirm("Add another item?");
    }

    if (cart.length === 0) {
      throw new ValidationError("Cart cannot be empty");
    }

    let grandTotal = cart.reduce((sum, item) => sum + item.totalPrice, 0);

    // -------- LAB 2: MEMBERSHIP DISCOUNT --------
    let membershipType = prompt("Membership Type (None/Silver/Gold/Platinum):");
    let discountFn = getDiscountFunction(membershipType);
    let discountAmount = discountFn(grandTotal);
    let discountedTotal = grandTotal - discountAmount;

    // -------- LAB 3: GST + PLATFORM FEE --------
    const gstRate = 0.18;
    const platformFeeRate = 0.002;

    let gstAmount = discountedTotal * gstRate;
    let platformFee = discountedTotal * platformFeeRate;
    let totalWithTax = discountedTotal + gstAmount + platformFee;

    // -------- LAB 4: PAYMENT MODE CHARGES --------
    let paymentMode = prompt("Payment Mode (Card/UPI/Cash):");
    let surcharge = 0;

    if (paymentMode === "Card" && totalWithTax < 1000) {
      surcharge = totalWithTax * 0.025;
    } else {
      surcharge = totalWithTax * 0.01;
    }

    let finalTotal = totalWithTax + surcharge;

    // -------- LAB 11: ASYNC PAYMENT --------
    let paymentStatus = await processPayment(paymentMode);
    console.log(paymentStatus);

    // -------- LAB 5: INVOICE GENERATION --------
    let invoice = {
      invoiceNumber: "INV-" + Math.floor(Math.random() * 100000),
      invoiceDate: new Date().toLocaleString(),
      items: cart,
      subtotal: grandTotal,
      discount: discountAmount,
      gst: gstAmount,
      platformFee,
      surcharge,
      finalAmount: finalTotal
    };

    console.table(cart);
    console.log("Invoice Summary:", invoice);
    console.log("Payment Successful | Invoice Generated");

    // -------- LAB 6 & 8: EMAIL VALIDATION --------
    let email;
    const emailRegex = /^[a-zA-Z0-9._%+-]+@karunya\.edu$/;

    do {
      email = prompt("Enter Karunya Email ID:");
      if (!emailRegex.test(email)) {
        alert("Invalid email. Use @karunya.edu");
      }
    } while (!emailRegex.test(email));

    console.log(`Invoice sent to ${email}`);
    console.log("Invoice JSON:");
    console.log(JSON.stringify(invoice, null, 2));

    // -------- LAB 7: SAVE TO LOCAL STORAGE --------
    localStorage.setItem("cartData", JSON.stringify(cart));
    localStorage.setItem("invoiceData", JSON.stringify(invoice));
    localStorage.setItem("email", email);

    // -------- LAB 13: CALLBACK --------
    completeBilling(() => {
      console.log("Thank you for shopping with Karazon.com!");
    });

  } catch (err) {
    console.error(`${err.name}: ${err.message}`);
  } finally {
    console.log("Billing session ended.");
  }
}

// -------------------- START APPLICATION --------------------
startBilling();