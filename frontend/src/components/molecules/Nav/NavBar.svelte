<script>
    import NavBarLinks from "../../atoms/Nav/NavBarLinks.svelte";
    import SearchBox from "../../molecules/Search/SearchBox.svelte";
</script>


<div class="nav-bar">
    <NavBarLinks />
    <SearchBox />
</div>

<style>
    .nav-bar {
        display: grid;
        grid: 'navlinks navlinks navlinks navlinks search';
        align-items: center;
        grid-area: navbar;
    }
</style>