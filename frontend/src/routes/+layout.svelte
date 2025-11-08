<script lang="ts">
	import '../app.css';
	import { favicon } from '$lib/assets';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<!-- Inter font (bold 700) for app typography -->
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@700&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

{@render children?.()}
