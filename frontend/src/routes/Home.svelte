<script>
    import fastapi from '../lib/api';
    import { tick } from 'svelte';
    // import { api_key } from '../lib/store';

    let urlInput = '';
    let summaryResult = '';
    let apiKey = '';
    let Buttondisabled = false;


  async function requestSummary(event) {
        event.preventDefault()
        Buttondisabled = true;
        let params = {
            url : urlInput,
            api_key: apiKey
        }
        
        fastapi('post', '/summary', params, (json) =>{
        summaryResult = json
        Buttondisabled = false;
        })
        
        
        
        
    }

</script>
<style>
  /* 컨테이너의 스타일을 추가하여 폼 요소들을 위아래로 배치합니다. */
  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
  }

  /* 스타일을 원하는대로 추가하세요 */
</style>



<div>
  <h1>LLMSummarizer</h1>
  <label for="textInput">youtube url:</label>
  <input type="text" id="textInput" bind:value={urlInput}/>
  
  <label for='apiKeyInput'>openai api key:</label>
  <input type='text' id='apiKeyInput' bind:value={apiKey}/>
  {#if apiKey !== '' && urlInput !== ''}
    <button on:click={requestSummary} disabled={Buttondisabled}>{Buttondisabled ? '처리중...' : '요약'}</button>
  {/if}
  {#if summaryResult !== ''}
    <h3>결과 : {summaryResult}</h3>
  {/if}
</div>

