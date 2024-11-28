<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-white">
    <!-- Header -->
    <h1 class="text-2xl font-bold text-gray-800 mb-4">DormMate Matching</h1>

    <!-- Sign Up Form -->
    <div class="w-full max-w-md bg-white p-6">
      <h2 class="text-xl font-semibold text-gray-800 mb-4">Sign up</h2>

      <form class="space-y-4">
        <!-- Mobile Number Input -->
        <div>
          <label for="mobile" class="block text-sm font-medium text-gray-700">
            Mobile Number
          </label>
          <div class="mt-1 relative">
            <input
              id="mobile"
              type="tel"
              placeholder="Mobile number"
              class="w-full border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>

        <!-- Verification Code -->
        <div>
          <label
            for="verification"
            class="block text-sm font-medium text-gray-700"
          >
            Verification Code
          </label>
          <div class="mt-1 flex">
            <input
              id="verification"
              type="text"
              placeholder="Enter code"
              class="flex-1 border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="button"
              class="bg-blue-500 text-white px-3 py-2 text-sm hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Get Code
            </button>
          </div>
        </div>

        <!-- Sign Up Button -->
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 text-sm font-medium hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Sign up
        </button>
      </form>

      <!-- Footer -->
      <div class="text-center mt-6">
        <a
          href="/login"
          class="text-sm text-gray-500 hover:text-blue-500 hover:underline"
        >
          I have account
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Sign Up - DormMate Matching'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
