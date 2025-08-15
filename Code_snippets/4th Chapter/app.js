const loadFleetBtn = document.getElementById('load-fleet-btn');
const fleetListContainer = document.getElementById('fleet-list');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const shipForm = document.getElementById('ship-form');
const saveBtn = document.getElementById('save-btn');
const cancelBtn = document.getElementById('cancel-btn');
const showCreateFormBtn = document.getElementById('show-create-form-btn');
const notificationArea = document.getElementById('notification-area');


function showNotification(message, isError = false) {
    notificationArea.textContent = message;
    notificationArea.style.color = isError ? '#ff6b6b' : '#6bff6b';
}

function openModalForCreate() {
    shipForm.reset();
    document.getElementById('ship-id').value = '';
    modalTitle.textContent = 'Launch a new spacecraft';
    modal.style.display = 'flex';
}

function openModalForEdit(ship) {
    shipForm.reset();
    document.getElementById('ship-id').value = ship.id;
    document.getElementById('ship-name').value = ship.name;
    document.getElementById('ship-type').value = ship.type;
    document.getElementById('ship-year').value = ship.launch_year;
    document.getElementById('ship-status').value = ship.status;
    modalTitle.textContent = `Editing: ${ship.name}`;
    modal.style.display = 'flex';
}

function closeModal() {
    modal.style.display = 'none';
    notificationArea.textContent = '';
}

function createShipCard(ship) {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
        <h3>${ship.name} (ID: ${ship.id})</h3>
        <p>Type: ${ship.type}</p>
        <p>Launch year: ${ship.launch_year}</p>
        <p>Status: ${ship.status}</p>
        <div class="card-actions">
            <button class="edit-btn" data-ship-id="${ship.id}">Edit</button>
            <button class="delete-btn" data-ship-id="${ship.id}">Decommission</button>
        </div>
    `;
    return card;
}

async function fetchAndDisplayFleet() {
    try {
        fleetListContainer.innerHTML = '<p>Loading telemetry...</p>';
        const ships = await apiRequest('/spaceships');

        fleetListContainer.innerHTML = '';
        if (ships.length === 0) {
            fleetListContainer.innerHTML = '<p>There are no spacecraft in the registry.</p>';
            return;
        }
        ships.forEach(ship => {
            const card = createShipCard(ship);
            fleetListContainer.appendChild(card);
        });
    } catch (error) {
        fleetListContainer.innerHTML = `<p style="color: #ff6b6b;">Error loading fleet: ${error.message}</p>`;
    }
}

async function handleSaveShip(event) {
    event.preventDefault();
    const shipId = document.getElementById('ship-id').value;
    const shipData = {
        name: document.getElementById('ship-name').value,
        type: document.getElementById('ship-type').value,
        launch_year: parseInt(document.getElementById('ship-year').value),
        status: document.getElementById('ship-status').value
    };

    try {
        let response;
        if (shipId) {
            response = await apiRequest(`/spaceships/${shipId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(shipData)
            });
            showNotification(`Spacecraft "${response.name}" updated successfully!`);
        } else {
            response = await apiRequest('/spaceships', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(shipData)
            });
            showNotification(`Spacecraft "${response.name}" launched successfully! ID: ${response.id}`);
        }

        setTimeout(() => {
            closeModal();
            fetchAndDisplayFleet();
        }, 1500);

    } catch (error) {
        showNotification(error.message, true);
    }
}

async function handleDeleteShip(shipId) {
    if (!confirm(`Are you sure you want to decommission spacecraft with ID ${shipId}?`)) return;

    try {
        await apiRequest(`/spaceships/${shipId}`, { method: 'DELETE' });
        alert('Spacecraft decommissioned successfully.');
        fetchAndDisplayFleet();
    } catch (error) {
        alert(`Error during decommissioning: ${error.message}`);
    }
}

document.addEventListener('DOMContentLoaded', fetchAndDisplayFleet);
loadFleetBtn.addEventListener('click', fetchAndDisplayFleet);
showCreateFormBtn.addEventListener('click', openModalForCreate);
cancelBtn.addEventListener('click', closeModal);
shipForm.addEventListener('submit', handleSaveShip);

fleetListContainer.addEventListener('click', async (event) => {
    const target = event.target;
    if (target.classList.contains('delete-btn')) {
        handleDeleteShip(target.dataset.shipId);
    }
    if (target.classList.contains('edit-btn')) {
        try {
            const ship = await apiRequest(`/spaceships/${target.dataset.shipId}`);
            openModalForEdit(ship);
        } catch (error) {
            alert(`Failed to load data for editing: ${error.message}`);
        }
    }
});
