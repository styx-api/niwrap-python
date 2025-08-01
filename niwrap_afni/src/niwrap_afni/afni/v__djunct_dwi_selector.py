# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DJUNCT_DWI_SELECTOR_METADATA = Metadata(
    id="5ab9f2d175d71ed28465ef305cf31b5079bd3841.boutiques",
    name="@djunct_dwi_selector",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VDjunctDwiSelectorParameters = typing.TypedDict('VDjunctDwiSelectorParameters', {
    "__STYXTYPE__": typing.Literal["@djunct_dwi_selector"],
    "dwi": InputPathType,
    "png": InputPathType,
    "outfile": str,
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
        "@djunct_dwi_selector": v__djunct_dwi_selector_cargs,
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
        "@djunct_dwi_selector": v__djunct_dwi_selector_outputs,
    }.get(t)


class VDjunctDwiSelectorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_dwi_selector(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """The main output file"""


def v__djunct_dwi_selector_params(
    dwi: InputPathType,
    png: InputPathType,
    outfile: str,
) -> VDjunctDwiSelectorParameters:
    """
    Build parameters.
    
    Args:
        dwi: Input DWI file.
        png: Output PNG image.
        outfile: Path to the output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_dwi_selector",
        "dwi": dwi,
        "png": png,
        "outfile": outfile,
    }
    return params


def v__djunct_dwi_selector_cargs(
    params: VDjunctDwiSelectorParameters,
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
    cargs.append("@djunct_dwi_selector.tcsh")
    cargs.append(execution.input_file(params.get("dwi")))
    cargs.append(execution.input_file(params.get("png")))
    cargs.append(params.get("outfile"))
    return cargs


def v__djunct_dwi_selector_outputs(
    params: VDjunctDwiSelectorParameters,
    execution: Execution,
) -> VDjunctDwiSelectorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctDwiSelectorOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(params.get("outfile")),
    )
    return ret


def v__djunct_dwi_selector_execute(
    params: VDjunctDwiSelectorParameters,
    execution: Execution,
) -> VDjunctDwiSelectorOutputs:
    """
    Selects DWI data and creates a representative image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctDwiSelectorOutputs`).
    """
    params = execution.params(params)
    cargs = v__djunct_dwi_selector_cargs(params, execution)
    ret = v__djunct_dwi_selector_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_dwi_selector(
    dwi: InputPathType,
    png: InputPathType,
    outfile: str,
    runner: Runner | None = None,
) -> VDjunctDwiSelectorOutputs:
    """
    Selects DWI data and creates a representative image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dwi: Input DWI file.
        png: Output PNG image.
        outfile: Path to the output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctDwiSelectorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_DWI_SELECTOR_METADATA)
    params = v__djunct_dwi_selector_params(
        dwi=dwi,
        png=png,
        outfile=outfile,
    )
    return v__djunct_dwi_selector_execute(params, execution)


__all__ = [
    "VDjunctDwiSelectorOutputs",
    "VDjunctDwiSelectorParameters",
    "V__DJUNCT_DWI_SELECTOR_METADATA",
    "v__djunct_dwi_selector",
    "v__djunct_dwi_selector_params",
]
