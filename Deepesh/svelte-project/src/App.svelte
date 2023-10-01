<script>
  let count = 0;

  function increment() {
    count += 1;
  }

  function decrement() {
    count -= 1;
  }
</script>

<main>
  <h1>Hello Svelte!</h1>
  <p>Count: {count}</p>
  <button on:click={increment}>Increment</button>
  <button on:click={decrement}>Decrement</button>
</main>

<style>
  main {
    text-align: center;
    padding: 20px;
  }
  button {
    font-size: 1.2rem;
    margin: 5px;
  }
</style>
