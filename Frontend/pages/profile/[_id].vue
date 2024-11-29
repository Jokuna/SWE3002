<template>
  <div class="flex flex-col min-h-screen bg-white">
    <!-- Header -->
    <!-- <div class="text-center border-b py-4 bg-white">
      <h1 class="text-xl font-bold text-gray-800">Details</h1>
    </div> -->

    <!-- Scrollable Content -->
    <div
      class="flex-1 overflow-y-auto px-6 py-4"
      style="max-height: calc(100vh - 150px)"
    >
      <!-- Profile Section -->
      <div class="flex flex-col items-center mb-6">
        <div class="w-24 h-24 rounded-full bg-gray-300 overflow-hidden">
          <!-- Placeholder for Profile Image -->
        </div>
        <p class="mt-4 text-lg font-medium text-gray-800">
          Hi, I&apos;m Hungry Donut.
        </p>
        <p class="text-gray-600">I am :</p>
      </div>

      <!-- Details Section -->
      <div class="space-y-3">
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Gender is Male</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">I would like to live in Ji-kwan</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">I am Smoker</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Not in Dormitory in weekend</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Bedtime is 23:00 ~ 07:00</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Age is private</p>
        </div>
        <div class="bg-gray-50 py-2 px-4 rounded">
          <p class="text-gray-800">Major is private</p>
        </div>
      </div>
    </div>

    <!-- Action Button -->
    <div class="px-6 py-4">
      <button
        type="button"
        class="w-full bg-blue-500 text-white py-3 rounded text-sm font-medium hover:bg-blue-600"
      >
        Gonna chat with her/him
      </button>
    </div>

    <!-- Bottom Navigation -->
    <div
      class="flex justify-around border-t bg-white py-4"
      style="padding-bottom: 0"
    >
      <button class="text-blue-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-blue-500 rounded-full"></div>
        <span class="text-xs mt-1">Search</span>
      </button>
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Message</span>
      </button>
      <button class="text-gray-500 flex flex-col items-center">
        <div class="w-6 h-6 bg-gray-300 rounded-full"></div>
        <span class="text-xs mt-1">Settings</span>
      </button>
    </div>
  </div>
</template>
