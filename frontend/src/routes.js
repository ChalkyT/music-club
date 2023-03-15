import AlbumPage from "./pages/AlbumPage.svelte";
import HomePage from "./pages/HomePage.svelte";
const routes = [
  {
    name: '/',
    component: HomePage
  },
  {
    name: 'album/:id',
    component: AlbumPage
  },
  {
    name: '404',
    path: '404',
    component: HomePage
  }
];

export {routes}