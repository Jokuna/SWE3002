<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-white">
    <!-- Header -->
    <h1 class="text-2xl font-bold text-gray-800 mb-4">DormMate Matching</h1>

    <!-- Login Form -->
    <div class="w-full max-w-md bg-white p-6">
      <h2 class="text-xl font-semibold text-gray-800 mb-4">Log in</h2>

      <form class="space-y-4">
        <!-- Email Input -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">
            Email Address
          </label>
          <div class="mt-1 relative">
            <input
              id="email"
              type="email"
              placeholder="Email"
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

        <!-- Login Button -->
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 text-sm font-medium hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Login
        </button>
      </form>

      <!-- Footer -->
      <div class="text-center mt-6">
        <NuxtLink
          to="/signup"
          class="text-sm text-gray-500 hover:text-blue-500 hover:underline"
        >
          I Don't Have Account
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Login - DormMate Matching'
    };
  }
};
</script>

<style>
/* Optional custom styles */
</style>
