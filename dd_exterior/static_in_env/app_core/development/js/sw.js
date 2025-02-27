const CACHE_NAME = 'cache-1.0';

const urlsToCache = [
  '/',

  // CSS
  "/static/app_core/assets/css/bootstrap.min.css",
  "/static/app_core/assets/css/all.min.css",
  "/static/app_core/assets/webfonts/flat-icon/flaticon_bantec.min.css",
  "/static/app_core/assets/css/animate.min.css",
  "/static/app_core/assets/css/swiper-bundle.min.css",
  "/static/app_core/assets/css/slick.min.css",
  "/static/app_core/assets/css/magnific-popup.min.css",
  "/static/app_core/assets/css/meanmenu.min.css",
  "/static/app_core/assets/css/style.min.css",
  "/static/app_user/vendors/pnotify/dist/pnotify.buttons.css",
  "/static/app_user/vendors/pnotify/dist/pnotify.nonblock.css",
  "/static/app_user/vendors/pnotify/dist/pnotify.brighttheme.css",
  "/static/app_core/development/css_whatsapp/whatsapp.min.css",
  "/static/app_core/development/css_whatsapp/line-awesome.min.css",
  "/static/app_core/development/css/lazy-loading.css",
  "/static/app_core/development/css/counters.min.css",
  "/static/app_core/development/css/modals.min.css",
  "/static/app_core/development/css/animation.min.css",
  "/static/app_core/development/css/preloaders.min.css",
  "/static/app_core/development/css/btns-fixed.min.css",
  "/static/app_core/development/css/easy-navigation.min.css",
  "/static/app_core/development/css/banner-home.css",
  "/static/app_core/development/css/social-media.min.css",
  "/static/app_core/development/css/responsive-default.min.css",
  "/static/app_core/development/css/section-media.min.css",
  "https://cdn.jsdelivr.net/npm/@fancyapps/ui/dist/fancybox.css",
  "https://fonts.googleapis.com/css2?family=Pacifico&display=swap",

  // JS
  "/static/app_core/assets/js/jquery-3.6.0.min.js",
  "/static/app_core/assets/js/bootstrap.min.js",
  "/static/app_core/assets/js/jquery.counterup.min.js",
  "/static/app_core/assets/js/popper.min.js",
  "/static/app_core/assets/js/progressbar.min.js",
  "/static/app_core/assets/js/jquery.magnific-popup.min.js",
  "/static/app_core/assets/js/swiper-bundle.min.js",
  "/static/app_core/assets/js/slick.min.js",
  "/static/app_core/assets/js/isotope.pkgd.min.js",
  "/static/app_core/assets/js/jquery.waypoints.min.js",
  "/static/app_core/assets/js/jquery.meanmenu.min.js",
  "/static/app_core/assets/js/custom.min.js",
  "/static/app_user/vendors/pnotify/dist/pnotify.js",
  "/static/app_user/vendors/pnotify/dist/pnotify.buttons.js",
  "/static/app_user/vendors/pnotify/dist/pnotify.nonblock.js",
  "/static/app_core/development/js/whatsapp.min.js",
  "/static/app_core/development/js/scroll-top.min.js",
  "/static/app_core/development/js/counters.min.js",
  "/static/app_core/development/js/observer-viewport.min.js",
  "/static/app_core/development/js/modals.min.js",
  "/static/app_core/development/js/preloaders.min.js",
  "/static/app_core/development/js/btns-fixed.min.js",
  "/static/app_core/development/js/easy-navigation.min.js",
  "/static/app_core/development/js/share-on-media.min.js",
  "/static/app_core/development/js/send-email.min.js",
  "/static/app_core/development/js/banner-home.min.js",
  "/static/app_core/development/js/lazy-loading.js",
  "https://cdn.jsdelivr.net/npm/@fancyapps/ui/dist/fancybox.umd.js"
];

// Instalar el Service Worker y almacenar archivos en caché
self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Interceptar solicitudes y servir desde caché si es posible
self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        // Si el archivo está en caché, servir desde caché
        if (response) {
          return response;
        }
        // Si no está en caché, realizar la solicitud de red normalmente
        return fetch(event.request);
      })
  );
});

// Actualizar el Service Worker y eliminar la caché anterior
self.addEventListener('activate', function (event) {
  const cacheWhitelist = [CACHE_NAME];

  event.waitUntil(
    caches.keys().then(function (cacheNames) {
      return Promise.all(
        cacheNames.map(function (cacheName) {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
