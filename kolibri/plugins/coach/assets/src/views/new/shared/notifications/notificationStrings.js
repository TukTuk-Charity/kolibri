import { createTranslator } from 'kolibri.utils.i18n';

/*
  nStrings.$tr('individualFinished', {learnerName, itemName})
  nStrings.$tr('multipleFinished', {learnerName, numOthers, itemName})
  nStrings.$tr('wholeClassFinished', {className, itemName})
  nStrings.$tr('wholeGroupFinished', {groupName, itemName})
  nStrings.$tr('everyoneFinished', {itemName})
  nStrings.$tr('individualNeedsHelp', {learnerName, itemName})
  nStrings.$tr('multipleNeedHelp', {learnerName, numOthers, itemName})
*/

const nStrings = createTranslator('CommonCoachStrings', {
  individualFinished: `{learnerName} finished '{itemName}'`,
  multipleFinished: `{learnerName} and {numOthers, number} {numOthers, plural, one {other} other {others}} finished '{itemName}'`,
  wholeClassFinished: `Everyone in '{className}' finished '{itemName}'`,
  wholeGroupFinished: `Everyone in '{groupName}' finished '{itemName}'`,
  everyoneFinished: `Everyone finished '{itemName}'`,
  individualNeedsHelp: `{learnerName} needs help with '{itemName}'`,
  multipleNeedHelp: `{learnerName} and {numOthers, number} {numOthers, plural, one {other} other {others}} need help with '{itemName}'`,
});

const nStringsMixin = {
  computed: {
    nStrings() {
      return nStrings;
    },
  },
};

export { nStrings, nStringsMixin };
