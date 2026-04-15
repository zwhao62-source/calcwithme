// Visitor Counter for CalcWithMe
// Uses countapi.xyz - free, no account required
(function() {
    'use strict';
    
    const NAMESPACE = 'calcwithme';
    const KEY = 'visitor-count';
    
    // Initialize counter if not exists
    async function initCounter() {
        try {
            // Try to get existing value
            let response = await fetch(`https://api.countapi.xyz/get/${NAMESPACE}/${KEY}`);
            
            if (response.status === 404) {
                // Create new counter
                response = await fetch(`https://api.countapi.xyz/create?namespace=${NAMESPACE}&key=${KEY}&enable_reset=1`);
                const data = await response.json();
                return data.value;
            }
            
            const data = await response.json();
            return data.value;
        } catch (e) {
            console.log('Visitor counter error:', e);
            return null;
        }
    }
    
    // Increment and get new count
    async function incrementCounter() {
        try {
            const response = await fetch(`https://api.countapi.xyz/hit/${NAMESPACE}/${KEY}`);
            const data = await response.json();
            return data.value;
        } catch (e) {
            console.log('Visitor counter error:', e);
            return null;
        }
    }
    
    // Display counter on page
    function displayCounter(count) {
        const counterEl = document.getElementById('visitor-counter');
        if (counterEl && count !== null) {
            counterEl.textContent = count.toLocaleString();
            counterEl.style.display = 'inline';
        }
    }
    
    // Initialize on page load
    async function init() {
        const count = await incrementCounter();
        displayCounter(count);
    }
    
    // Run
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
