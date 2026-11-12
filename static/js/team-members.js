const membersButton = document.querySelector('.members-button');
const memberList = document.querySelector('#member-list');

if (membersButton && memberList) {
    membersButton.addEventListener('click', () => {
        const isExpanded = membersButton.getAttribute('aria-expanded') === 'true';
        membersButton.setAttribute('aria-expanded', String(!isExpanded));
        membersButton.textContent = isExpanded ? 'See members' : 'Hide members';
        memberList.hidden = isExpanded;
    });
}
