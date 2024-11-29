<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-white">
    <!-- Header -->
    <h1 class="text-4xl font-bold text-gray-800 mb-4">SKKU-Dormie</h1>
    <p class="text-base font-bold text-gray-800 mb-4">for find dormate</p>

    <!-- Sign Up Form -->
    <div class="w-full max-w-md bg-white p-6">
      <h2 class="text-xl font-semibold text-gray-800 mb-4">Sign up</h2>

      <form class="space-y-4">
        <!-- Email Number Input -->
        <div>
          <!-- <label for="email" class="block text-sm font-medium text-gray-700">
            Email Address
          </label> -->
          <div class="mt-1 relative">
            <input
              id="email"
              type="email"
              placeholder="Email Address"
              class="w-full border border-gray-300 p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>

        <!-- Verification Code -->
        <div>
          <!-- <label
            for="verification"
            class="block text-sm font-medium text-gray-700"
          >
            Verification Code
          </label> -->
          <div class="mt-1 flex">
            <input
              id="verification"
              type="text"
              placeholder="Verification Code"
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

      <div class="flex justify-center mt-6">
        <img src="/skku_logo.jpg" alt="SKKU Logo" class="h-32" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'SKKU-Dormie for find dormate'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
