chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url) {
    try {
      const response = await fetch('http://127.0.0.1:8000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: tab.url })
      });
      const result = await response.json();

      if (result.safe === false) {
        chrome.notifications.create({
          type: 'basic',
          iconUrl: 'icon.png',
          title: 'AI Web Guardian',
          message: result.message
        });

        setTimeout(() => {
          chrome.tabs.remove(tabId);
        }, 2000);
      }
    } catch (e) {
      console.error('Error:', e);
    }
  }
});
