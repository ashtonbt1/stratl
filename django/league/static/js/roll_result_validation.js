
var modOptions = ['Normal', 'Split', 'Ballpark Single', 'Ballpark Open', 'Ballpark HR', 'Ballpark HR Split', 'Injury Chance', 'Clutch', 'Fatigue'];

var modShortcuts = {
	'n': 'Normal',
  's': 'Split',
  'bs': 'Ballpark Single',
  'bo': 'Ballpark Open',
  'bh': 'Ballpark HR',
  'bhs': 'Ballpark HR Split',
  'i': 'Injury Chance',
  'inj': 'Injury Chance',
  'c': 'Clutch',
  'cl': 'Clutch',
  'f': 'Fatigue'
}

var resultShortcuts = {
	'xca': 'CATCH-X',
  'xp': 'GB (p) X',
  'x1': 'GB (1b) X',
  'x1b': 'GB (1b) X',
  'x2': 'GB (2b) X',
  'x2b': 'GB (2b) X',
  'x3': 'GB (3b) X',
  'x3b': 'GB (3b) X',
  'xs': 'GB (ss) X',
  'xss': 'GB (ss) X',
  'xlf': 'FLY (lf) X',
  'x7': 'FLY (lf) X',
  'xcf': 'FLY (cf) X',
  'x8': 'FLY (cf) X',
  'xrf': 'FLY (rf) X',
  'x9': 'FLY (rf) X',
  'do': 'DO',
  'do..': 'DO**',
  'do--': 'DO**',
  'dbl': 'DOUBLE**',
  'dbl--': 'DOUBLE**',
  'dbl..': 'DOUBLE**',
  'do7': 'DOUBLE (lf)',
  'do lf': 'DOUBLE (lf)',
  'do8': 'DOUBLE (cf)',
  'do cf': 'DOUBLE (cf)',
  'do9': 'DOUBLE (rf)',
  'do rf': 'DOUBLE (rf)',
  'hbp': 'HBP',
  'home': 'HOMERUN',
  'hr': 'HR',
  'nhr': 'N-HR',
  'n-hr': 'N-HR',
  'si.': 'SI*',
  'si-': 'SI*',
  'si..': 'SI**',
  'si--': 'SI**',
  'si7': 'SINGLE (lf)',
  'si lf': 'SINGLE (lf)',
  'si8': 'SINGLE (cf)',
  'si cf': 'SINGLE (cf)',
  'si9': 'SINGLE (rf)',
  'si rf': 'SINGLE (rf)',
  'sin.': 'SINGLE*',
  'sin..': 'SINGLE**',
  'tr': 'TR',
  'triple': 'TRIPLE',
  'trip': 'TRIPLE',
  'walk': 'WALK',
  'bb': 'WALK',
  'w': 'WALK',
  'fla': 'fly (lf) A',
  'f lf a': 'fly (lf) A',
  'flb': 'fly (lf) B',
  'f lf b': 'fly (lf) B',
  'flb.': 'fly (lf) B?',
  'flb/': 'fly (lf) B?',
  'flb?': 'fly (lf) B?',
  'f lf b/': 'fly (lf) B?',
  'f lf b?': 'fly (lf) B?',
  'flc': 'fly (lf) C',
  'f lf c': 'fly (lf) C',
  'fca': 'fly (cf) A',
  'f cf a': 'fly (cf) A',
  'fcb': 'fly (cf) B',
  'f cf b': 'fly (cf) B',
  'fcb.': 'fly (cf) B?',
  'fcb/': 'fly (cf) B?',
  'fcb?': 'fly (cf) B?',
  'f cf b/': 'fly (cf) B?',
  'f cf b?': 'fly (cf) B?',
  'fcc': 'fly (cf) C',
  'f cf c': 'fly (cf) C',
  'fra': 'fly (rf) A',
  'f rf a': 'fly (rf) A',
  'frb': 'fly (rf) B',
  'f rf b': 'fly (rf) B',
  'frb.': 'fly (rf) B?',
  'frb/': 'fly (rf) B?',
  'frb?': 'fly (rf) B?',
  'f rf b/': 'fly (rf) B?',
  'f rf b?': 'fly (rf) B?',
  'frc': 'fly (rf) C',
  'f rf c': 'fly (rf) C',
  'fo1b': 'foulout (1b)',
  'fo1': 'foulout (1b)',
  'fo 1b': 'foulout (1b)',
  'fo 1': 'foulout (1b)',
  'fo3b': 'foulout (3b)',
  'fo3': 'foulout (3b)',
  'fo 3b': 'foulout (3b)',
  'fo 3': 'foulout (3b)',
  'foc': 'foulout (c)',
  'fo c': 'foulout (c)',
  'gpa': 'gb (p) A',
  'g p a': 'gb (p) A',
  'gpb': 'gb (p) B',
  'g p b': 'gb (p) B',
  'g1a': 'gb (1b) A',
  'g 1b a': 'gb (1b) A',
  'g 1 a': 'gb (1b) A',
  'g1a.': 'gb (1b) A+',
  'g 1b a.': 'gb (1b) A+',
  'g 1 a.': 'gb (1b) A+',
  'g1a-': 'gb (1b) A+',
  'g 1b a-': 'gb (1b) A+',
  'g 1 a-': 'gb (1b) A+',
  'g1a=': 'gb (1b) A+',
  'g 1b a=': 'gb (1b) A+',
  'g 1 a=': 'gb (1b) A+',
  'g1a+': 'gb (1b) A+',
  'g 1b a+': 'gb (1b) A+',
  'g 1 a+': 'gb (1b) A+',
  'g1b': 'gb (1b) B',
  'g 1b b': 'gb (1b) B',
  'g 1 b': 'gb (1b) B',
  'g1c': 'gb (1b) C',
  'g 1b c': 'gb (1b) C',
  'g 1 c': 'gb (1b) C',
  'g2a': 'gb (2b) A',
  'g 2b a': 'gb (2b) A',
  'g 2 a': 'gb (2b) A',
  'g2a.': 'gb (2b) A+',
  'g 2b a.': 'gb (2b) A+',
  'g 2 a.': 'gb (2b) A+',
  'g2a-': 'gb (2b) A+',
  'g 2b a-': 'gb (2b) A+',
  'g 2 a-': 'gb (2b) A+',
  'g2a=': 'gb (2b) A+',
  'g 2b a=': 'gb (2b) A+',
  'g 2 a=': 'gb (2b) A+',
  'g2a+': 'gb (2b) A+',
  'g 2b a+': 'gb (2b) A+',
  'g 2 a+': 'gb (2b) A+',
  'g2b': 'gb (2b) B',
  'g 2b b': 'gb (2b) B',
  'g 2 b': 'gb (2b) B',
  'g2b.': 'gb (2b) B+',
  'g 2b b.': 'gb (2b) B+',
  'g 2 b.': 'gb (2b) B+',
  'g2b-': 'gb (2b) B+',
  'g 2b b-': 'gb (2b) B+',
  'g 2 b-': 'gb (2b) B+',
  'g2b=': 'gb (2b) B+',
  'g 2b b=': 'gb (2b) B+',
  'g 2 b=': 'gb (2b) B+',
  'g2b+': 'gb (2b) B+',
  'g 2b b+': 'gb (2b) B+',
  'g 2 b+': 'gb (2b) B+',
  'g2c': 'gb (2b) C',
  'g 2b c': 'gb (2b) C',
  'g 2 c': 'gb (2b) C',
  'gsa': 'gb (ss) A',
  'g ss a': 'gb (ss) A',
  'g s a': 'gb (ss) A',
  'gsa.': 'gb (ss) A+',
  'g ss a.': 'gb (ss) A+',
  'g s a.': 'gb (ss) A+',
  'gsa-': 'gb (ss) A+',
  'g ss a-': 'gb (ss) A+',
  'g s a-': 'gb (ss) A+',
  'gsa=': 'gb (ss) A+',
  'g ss a=': 'gb (ss) A+',
  'g s a=': 'gb (ss) A+',
  'gsa+': 'gb (ss) A+',
  'g ss a+': 'gb (ss) A+',
  'g s a+': 'gb (ss) A+',
  'gsb': 'gb (ss) B',
  'g ss b': 'gb (ss) B',
  'g s b': 'gb (ss) B',
  'gsb.': 'gb (ss) B+',
  'g ss b.': 'gb (ss) B+',
  'g s b.': 'gb (ss) B+',
  'gsb-': 'gb (ss) B+',
  'g ss b-': 'gb (ss) B+',
  'g s b-': 'gb (ss) B+',
  'gsb=': 'gb (ss) B+',
  'g ss b=': 'gb (ss) B+',
  'g s b=': 'gb (ss) B+',
  'gsb+': 'gb (ss) B+',
  'g ss b+': 'gb (ss) B+',
  'g s b+': 'gb (ss) B+',
  'g3a': 'gb (3b) A',
  'g 3b a': 'gb (3b) A',
  'g 3 a': 'gb (3b) A',
  'g3b': 'gb (3b) B',
  'g 3b b': 'gb (3b) B',
  'g 3 b': 'gb (3b) B',
  'lin1': 'lineout (1b)',
  'lineout1': 'lineout (1b)',
  'lin 1': 'lineout (1b)',
  'lin2': 'lineout (2b)',
  'lineout2': 'lineout (2b)',
  'lin 2': 'lineout (2b)',
  'lin3': 'lineout (3b)',
  'lineout3': 'lineout (3b)',
  'lin 3': 'lineout (3b)',
  'lins': 'lineout (ss)',
  'lineouts': 'lineout (ss)',
  'lin s': 'lineout (ss)',
  'linss': 'lineout (ss)',
  'lineoutss': 'lineout (ss)',
  'lin ss': 'lineout (ss)',
  'lineout ss': 'lineout (ss)',
  'lo': 'lo',
  'l1': 'lo (1b)',
  'lo1': 'lo (1b)',
  'lo 1': 'lo (1b)',
  'l2': 'lo (2b)',
  'lo2': 'lo (2b)',
  'lo 2': 'lo (2b)',
  'l3': 'lo (3b)',
  'lo3': 'lo (3b)',
  'lo 3': 'lo (3b)',
  'ls': 'lo (ss)',
  'los': 'lo (ss)',
  'lo s': 'lo (ss)',
  'loss': 'lo (ss)',
  'lo ss': 'lo (ss)',
  'l1m': 'lo (1b) max',
  'lo1m': 'lo (1b) max',
  'lo 1 max': 'lo (1b) max',
  'lo 1 m': 'lo (1b) max',
  'l2m': 'lo (2b) max',
  'lo2m': 'lo (2b) max',
  'lo 2 max': 'lo (2b) max',
  'lo 2 m': 'lo (2b) max',
  'l3m': 'lo (3b) max',
  'lo3m': 'lo (3b) max',
  'lo 3 max': 'lo (3b) max',
  'lo 3 m': 'lo (3b) max',
  'lsm': 'lo (ss) max',
  'losm': 'lo (ss) max',
  'lo s max': 'lo (ss) max',
  'lo s m': 'lo (ss) max',
  'lssm': 'lo (ss) max',
  'lossm': 'lo (ss) max',
  'lo ss max': 'lo (ss) max',
  'lo ss m': 'lo (ss) max',
  'p1': 'popout (1b)',
  'po1': 'popout (1b)',
  'p1b': 'popout (1b)',
  'pop 1b': 'popout (1b)',
  'p2': 'popout (2b)',
  'po2': 'popout (2b)',
  'p2b': 'popout (2b)',
  'pop 2b': 'popout (2b)',
  'p3': 'popout (3b)',
  'po3': 'popout (3b)',
  'p3b': 'popout (3b)',
  'pop 3b': 'popout (3b)',
  'ps': 'popout (ss)',
  'pos': 'popout (ss)',
  'pss': 'popout (ss)',
  'pop ss': 'popout (ss)',
  'so': 'strikeout',
  'k': 'strikeout'
}

var disableFields = {
	'Normal': ['low', 'split', 'high'],
  'Split': ['description'],
  'Ballpark Single': ['low', 'split', 'high'],
  'Ballpark Open': [],
  'Ballpark HR': ['low', 'split', 'high'],
  'Ballpark HR Split': ['description'],
  'Injury Chance': ['low', 'split', 'high'],
  'Clutch': ['low', 'split', 'high'],
  'Fatigue': ['low', 'split', 'high'],
};

function disableForMods(fields, arr) {
	console.log(arr);
	arr.forEach(val => {
  	console.log(fields);
  	fields[val].disabled = true;
    fields[val].style.backgroundColor = '#CCCCCC';
	});
}

function validateMod(el) {
	// Get the parent form and make sure it's the correct object
	var rollForm = el.parentNode;
  if (rollForm.className.includes('roll-result')) {
  } else {
  	return;
  }
  // Create an object with one key per field
  var formFields = {};
  for (i=0; i<rollForm.children.length; i++) {
  	formFields[rollForm.children[i].name] = rollForm.children[i];
  }
  // Do a quick replacement of shortcuts for the modifiers
  if (formFields.modifier.value in modShortcuts) {
  	formFields.modifier.value = modShortcuts[formFields.modifier.value];
  }
  // Do the same for description, low, and high
  if ((formFields.description.value in resultShortcuts) && (!formFields.description.disabled)) {
  	formFields.description.value = resultShortcuts[formFields.description.value];
  }
  if ((formFields.low.value in resultShortcuts) && (!formFields.low.disabled)) {
  	formFields.low.value = resultShortcuts[formFields.low.value];
  }
  if ((formFields.high.value in resultShortcuts) && (!formFields.high.disabled)) {
  	formFields.high.value = resultShortcuts[formFields.high.value];
  }
  // Disable all fields if modifier is not valid
  if (!modOptions.includes(formFields.modifier.value)) {
  	formFields.modifier.style.borderColor = '#FF0000';
    var disFields = ['description', 'split', 'low', 'high'];
  	disFields.forEach(val => {
    	formFields[val].disabled = true;
      formFields[val].style.backgroundColor = '#CCCCCC';
	});
  // Reference the disableFields reference object to get which fields should be active and not
  } else {
  	formFields.modifier.style.borderColor = '#00FF00';
    var totFields = ['description', 'split', 'low', 'high'];
    var disFields = disableFields[formFields.modifier.value];
  	totFields.forEach(val => {
    	if (disFields.includes(val)) {
        formFields[val].disabled = true;
        formFields[val].style.backgroundColor = '#CCCCCC';
      } else {
      	formFields[val].disabled = false;
        formFields[val].style.backgroundColor = null;
      }
    });
  }
/*   if (!modOptions.includes(formFields.modifier.value)) {
    var disFields = ['desc', 'split', 'low', 'high'];
    disableForMods(formFields, disFields);
  } */
/*   if (formFields.modifier.value == 'Normal') {
    var disFields = ['low', 'split', 'high'];
    disFields.forEach(val => {
      formFields[val].disabled = true;
      formFields[val].style.backgroundColor = '#CCCCCC';
    });
  } else if ((formFields.modifier.value == 'Split')) {
    var disFields = ['desc'];
    disFields.forEach(val => {
      formFields[val].disabled = true;
      formFields[val].style.backgroundColor = '#CCCCCC';
  } */
  /* Array.from(rollForms[0].children).forEach(x => {
    console.log(x.placeholder);
  }); */
/*   for (i=0; i<modFields.length; i++) {
    if (!modOptions.includes(modFields[i].value)) {
      modFields[i].style.borderColor = '#FF0000';
    } else {
      modFields[i].style.borderColor = '#00FF00';
    }
  } */

}