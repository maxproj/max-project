var window_objects = []; /* массив всех открываемых окон */
 
function windowOpenExample(event) {
  event.preventDefault(); /* отмена действий браузера по умолчанию */
  var ref_href = event.currentTarget.href; /* URL из ссылки */
  var ref_target = event.currentTarget.target; /* имя окна из ссылки */
 
  if ((window_objects[ref_target] == undefined) || window_objects[ref_target].closed) {
    /* если окно ещё не открыто или уже закрыто, тогда можно задать параметры для окна */
    window_objects[ref_target] = window.open(
      ref_href,
      ref_target,
      'top=0,left=0,height=400,width=400,resizable,scrollbars,status'
    );
    window_objects[ref_target].moveTo(0, 0);
    window_objects[ref_target].resizeTo(400, 400);
  } else {
    /* если окно открыто, тогда его параметры изменить нельзя */
    window_objects[ref_target] = window.open(
      ref_href,
      ref_target
    );
  }
 
  window_objects[ref_target].focus(); /* фокусировка на окне */
}