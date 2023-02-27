<script>
    // Hardcoded data for now. TODO: Implement loading data from json with defaults for missing data.
    let albumArt = 'https://upload.wikimedia.org/wikipedia/en/f/f8/10000Days.jpg';
    let title = '10000 Days';
    let artist = 'Tool';
    let genre = 'Progressive Metal/Rock'
    let about = 'Overrated? Not at all! It\'s not my fault you can\'t pay attention to songs over 3 minutes long.'
</script>

<div class="album-container">
    <header class="album-title">
        <h2>{title} - {artist}</h2>
        <p>{genre}</p>
    </header>
    <main>
        <div class="album-art">
            <img src="{albumArt}" alt="Album art for {title} by {artist}" />
        </div>
        <div class="about-album-text">
            <p>{about}</p>
        </div>
    </main>
</div>


<style>
    .album-container {
        width: 100%;
        border: #FF0000 solid 1px;
    }
</style>