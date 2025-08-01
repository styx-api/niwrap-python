# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

QUANTIFY_THALAMIC_NUCLEI_SH_METADATA = Metadata(
    id="c597d875efd70402af0d29eccadf64e0e07bc431.boutiques",
    name="quantifyThalamicNuclei.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


QuantifyThalamicNucleiShParameters = typing.TypedDict('QuantifyThalamicNucleiShParameters', {
    "__STYXTYPE__": typing.Literal["quantifyThalamicNuclei.sh"],
    "output_file": str,
    "analysis_id": str,
    "subjects_directory": typing.NotRequired[str | None],
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
        "quantifyThalamicNuclei.sh": quantify_thalamic_nuclei_sh_cargs,
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
        "quantifyThalamicNuclei.sh": quantify_thalamic_nuclei_sh_outputs,
    }.get(t)


class QuantifyThalamicNucleiShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quantify_thalamic_nuclei_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """The output file containing quantified thalamic nuclei results."""


def quantify_thalamic_nuclei_sh_params(
    output_file: str,
    analysis_id: str,
    subjects_directory: str | None = None,
) -> QuantifyThalamicNucleiShParameters:
    """
    Build parameters.
    
    Args:
        output_file: Output file for the results.
        analysis_id: Analysis ID for specificity.
        subjects_directory: Directory containing subject data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "quantifyThalamicNuclei.sh",
        "output_file": output_file,
        "analysis_id": analysis_id,
    }
    if subjects_directory is not None:
        params["subjects_directory"] = subjects_directory
    return params


def quantify_thalamic_nuclei_sh_cargs(
    params: QuantifyThalamicNucleiShParameters,
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
    cargs.append("quantifyThalamicNuclei.sh")
    cargs.append(params.get("output_file"))
    cargs.append(params.get("analysis_id"))
    if params.get("subjects_directory") is not None:
        cargs.append(params.get("subjects_directory"))
    return cargs


def quantify_thalamic_nuclei_sh_outputs(
    params: QuantifyThalamicNucleiShParameters,
    execution: Execution,
) -> QuantifyThalamicNucleiShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = QuantifyThalamicNucleiShOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file(params.get("output_file")),
    )
    return ret


def quantify_thalamic_nuclei_sh_execute(
    params: QuantifyThalamicNucleiShParameters,
    execution: Execution,
) -> QuantifyThalamicNucleiShOutputs:
    """
    Command-line tool to quantify thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `QuantifyThalamicNucleiShOutputs`).
    """
    params = execution.params(params)
    cargs = quantify_thalamic_nuclei_sh_cargs(params, execution)
    ret = quantify_thalamic_nuclei_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def quantify_thalamic_nuclei_sh(
    output_file: str,
    analysis_id: str,
    subjects_directory: str | None = None,
    runner: Runner | None = None,
) -> QuantifyThalamicNucleiShOutputs:
    """
    Command-line tool to quantify thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_file: Output file for the results.
        analysis_id: Analysis ID for specificity.
        subjects_directory: Directory containing subject data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuantifyThalamicNucleiShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUANTIFY_THALAMIC_NUCLEI_SH_METADATA)
    params = quantify_thalamic_nuclei_sh_params(
        output_file=output_file,
        analysis_id=analysis_id,
        subjects_directory=subjects_directory,
    )
    return quantify_thalamic_nuclei_sh_execute(params, execution)


__all__ = [
    "QUANTIFY_THALAMIC_NUCLEI_SH_METADATA",
    "QuantifyThalamicNucleiShOutputs",
    "QuantifyThalamicNucleiShParameters",
    "quantify_thalamic_nuclei_sh",
    "quantify_thalamic_nuclei_sh_params",
]
