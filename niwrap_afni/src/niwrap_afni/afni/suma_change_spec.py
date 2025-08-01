# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SUMA_CHANGE_SPEC_METADATA = Metadata(
    id="f13f0176c0f78fdf29d29c5c7899209d6deff415.boutiques",
    name="suma_change_spec",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SumaChangeSpecParameters = typing.TypedDict('SumaChangeSpecParameters', {
    "__STYXTYPE__": typing.Literal["suma_change_spec"],
    "input": InputPathType,
    "state": str,
    "domainparent": typing.NotRequired[str | None],
    "output": typing.NotRequired[str | None],
    "remove": bool,
    "anatomical": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "suma_change_spec": suma_change_spec_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "suma_change_spec": suma_change_spec_outputs,
    }.get(t)


class SumaChangeSpecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `suma_change_spec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_spec: OutputPathType | None
    """New Spec file"""
    backup_spec: OutputPathType
    """Backup of the original Spec file"""


def suma_change_spec_params(
    input_: InputPathType,
    state: str,
    domainparent: str | None = None,
    output: str | None = None,
    remove: bool = False,
    anatomical: bool = False,
) -> SumaChangeSpecParameters:
    """
    Build parameters.
    
    Args:
        input_: SUMA Spec file to change.
        state: State within the Spec file to change.
        domainparent: New Domain Parent for the state within the Spec file.
        output: Name to which the new Spec file will be temporarily written.
        remove: Remove the automatically created backup.
        anatomical: Add 'Anatomical = Y' to the selected SurfaceState.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "suma_change_spec",
        "input": input_,
        "state": state,
        "remove": remove,
        "anatomical": anatomical,
    }
    if domainparent is not None:
        params["domainparent"] = domainparent
    if output is not None:
        params["output"] = output
    return params


def suma_change_spec_cargs(
    params: SumaChangeSpecParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("suma_change_spec")
    cargs.append(execution.input_file(params.get("input")))
    cargs.append(params.get("state"))
    if params.get("domainparent") is not None:
        cargs.append(params.get("domainparent"))
    if params.get("output") is not None:
        cargs.append(params.get("output"))
    if params.get("remove"):
        cargs.append("-remove")
    if params.get("anatomical"):
        cargs.append("-anatomical")
    return cargs


def suma_change_spec_outputs(
    params: SumaChangeSpecParameters,
    execution: Execution,
) -> SumaChangeSpecOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SumaChangeSpecOutputs(
        root=execution.output_file("."),
        output_spec=execution.output_file(params.get("output")) if (params.get("output") is not None) else None,
        backup_spec=execution.output_file(pathlib.Path(params.get("input")).name + ".bkp"),
    )
    return ret


def suma_change_spec_execute(
    params: SumaChangeSpecParameters,
    execution: Execution,
) -> SumaChangeSpecOutputs:
    """
    This program changes SUMA's surface specification (Spec) files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SumaChangeSpecOutputs`).
    """
    params = execution.params(params)
    cargs = suma_change_spec_cargs(params, execution)
    ret = suma_change_spec_outputs(params, execution)
    execution.run(cargs)
    return ret


def suma_change_spec(
    input_: InputPathType,
    state: str,
    domainparent: str | None = None,
    output: str | None = None,
    remove: bool = False,
    anatomical: bool = False,
    runner: Runner | None = None,
) -> SumaChangeSpecOutputs:
    """
    This program changes SUMA's surface specification (Spec) files.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_: SUMA Spec file to change.
        state: State within the Spec file to change.
        domainparent: New Domain Parent for the state within the Spec file.
        output: Name to which the new Spec file will be temporarily written.
        remove: Remove the automatically created backup.
        anatomical: Add 'Anatomical = Y' to the selected SurfaceState.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SumaChangeSpecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUMA_CHANGE_SPEC_METADATA)
    params = suma_change_spec_params(
        input_=input_,
        state=state,
        domainparent=domainparent,
        output=output,
        remove=remove,
        anatomical=anatomical,
    )
    return suma_change_spec_execute(params, execution)


__all__ = [
    "SUMA_CHANGE_SPEC_METADATA",
    "SumaChangeSpecOutputs",
    "SumaChangeSpecParameters",
    "suma_change_spec",
    "suma_change_spec_params",
]
