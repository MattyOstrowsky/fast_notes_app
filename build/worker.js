var CACHE_NAME = 'pwa-task-manager';
var RUNTIME = 'runtime';
var urlsToCache = [
  '/',
  '/completed',
  'index.html',
  '/login',
  '/auth/users/me/',
  '/favicon.ico',
  '/logo192.png'
];

// Install a service worker
self.addEventListener('install', event => {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Cache and return requests
self.addEventListener('fetch', event => {
  console.log('[Service Worker] Fetch event for ', event.request.url);
  event.respondWith((async () => {
    const cachedResponse = await caches.match(event.request);
    console.log(`[Service Worker] Fetching resource: ${event.request.url}`);
    if (cachedResponse) {
      return cachedResponse;
    }
  
    const response = await fetch(event.request);
  
    if (!response || response.status !== 200 || response.type !== 'basic') {
      return response;
    }
  

    const responseToCache = response.clone();
    const cache = await caches.open(RUNTIME)
    console.log(`[Service Worker] Caching new resource: ${event.request.url}`);
    await cache.put(event.request, response.clone());
    
  
    return response;
  })());
});

// Update a service worker
self.addEventListener('activate', event => {
  var cacheWhitelist = ['pwa-task-manager'];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener('launch', event => {
  event.handleLaunch((async () => {
    // Get an existing client.
    const client = (await clients.matchAll())[0];

    if (client) {
      client.focus();
      client.postMessage('search');
    } else {
      clients.openWindow(event.url);
    }
  })());
});