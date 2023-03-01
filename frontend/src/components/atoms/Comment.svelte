<script>
    export let comment;
    export let user;
    export let id;
</script>

<div class="comment" id={id}>
    {#if !user}
        <p>{comment}</p>
    {:else}
        <span>{user}</span>
        <p>{comment}</p>
    {/if}
</div>

<style>
   .comment {
       background-color: #f7e1b5;
       padding: 1rem;
       margin-bottom: 1rem;
   }
   span {
       font-size: 0.6rem;
   }
   p {
       font-size: 0.8rem;
   }
</style>


