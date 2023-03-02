<script>
    import SearchButton from "../../atoms/Search/SearchButton.svelte";
    import SearchInput from "../../atoms/Search/SearchInput.svelte";
</script>

<form class="search-box">
    <SearchInput />
    <SearchButton />
</form>

<style>
    .search-box {
        border-radius: 10px;
        border: solid black 1px;
        overflow: hidden;
        height: 100%;
        display: grid;
        width: 30%;
        grid: 'button input input input';
        grid-area: search;
    }
</style>
