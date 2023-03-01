<script>
    import Comment from "../atoms/Comment.svelte";
    import CommentCount from "../atoms/CommentCount.svelte";

    export let comments = [];
</script>
<!--If the comment array is empty (no data), show a single comment telling the user about the lack of comments-->
{#if comments.length === 0}
    <Comment user={false} comment={"No comments :("} id={"no_comments"}/>
{:else}
    <CommentCount commentCount={comments.length} />
    <div class="comments">
        {#each comments as comment, index}
            <Comment user={comment.user} comment={comment.comment} id={`comment_${index + 1}`} />
        {/each}
    </div>
{/if}

<style>

</style>